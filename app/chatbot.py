from groq import Groq
from app.config import GROQ_API_KEY
from app.database import mongo_db

class Chatbot:
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)

    def generate_response(self, user_id: str, user_message: str) -> str:
        # Rule-based responses for common e-commerce questions
        message_lower = user_message.lower()
        if "track my order" in message_lower:
            bot_response = "To track your order, visit our website, click 'Track Order' in the menu, and enter your order number and email address. You’ll see the current status and estimated delivery date."
        elif "status of my order" in message_lower:
            bot_response = "Please provide your order number and email address, or log in to your account and check the 'Order History' section for the status of your order."
        elif "shipping take" in message_lower:
            bot_response = "Shipping typically takes 3-7 business days, depending on your location and selected shipping method. You can view estimated delivery times at checkout or in your order confirmation email."
        elif "request a refund" in message_lower:
            bot_response = "To request a refund, log in to your account, go to 'Order History,' select the order, and click 'Request Refund.' Follow the prompts to submit your request. Refunds are processed within 5-10 business days."
        elif "return policy" in message_lower:
            bot_response = "Our return policy allows returns within 30 days of delivery for unused items in original packaging. Visit our 'Returns' page to start a return and obtain a prepaid shipping label."
        elif "in stock" in message_lower:
            bot_response = "Please check the product page on our website for real-time stock status. If it’s out of stock, you can sign up for restock notifications."
        elif "payment declined" in message_lower:
            bot_response = "A payment may be declined due to insufficient funds, incorrect card details, or bank restrictions. Please verify your payment information or try another payment method. Contact our support team for further assistance."
        elif "contact customer support" in message_lower:
            bot_response = "You can reach our customer support team via email at support@ecommerce.com, by phone at 1-800-123-4567 (Mon-Fri, 9 AM-5 PM), or through the 'Contact Us' form on our website."
        elif "promo code" in message_lower:
            bot_response = "To apply a promo code, add items to your cart, proceed to checkout, and enter the code in the 'Promo Code' field. The discount will be applied if the code is valid."
        elif "forgot my password" in message_lower:
            bot_response = "To reset your password, click 'Login' on our website, then select 'Forgot Password.' Enter your email address, and we’ll send you a link to reset your password."
        else:
            # Fetch conversation history for context (limit to last 5 messages)
            history = mongo_db.get_conversation_history(user_id, limit=5)
            context = "\n".join([f"User: {conv['user_message']}\nBot: {conv['bot_response']}" for conv in history])

            # Create prompt for Groq API
            prompt = f"""
            You are a customer support chatbot for an e-commerce website. Provide polite, concise, and accurate answers. 
            NEVER mention errors or technical difficulties unless the user reports a specific issue.
            Use the following conversation history for context, if relevant:
            {context}

            User: {user_message}
            Bot:
            """

            # Call Groq API
            try:
                response = self.client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": "You are a customer support assistant for an e-commerce website."},
                        {"role": "user", "content": prompt}
                    ],
                    model="llama-3.3-70b-versatile",
                    max_tokens=500
                )
                bot_response = response.choices[0].message.content.strip()
            except Exception as e:
                bot_response = "Sorry, I couldn't process your request due to a technical issue. Please try again or contact support."

        # Save conversation to MongoDB
        mongo_db.save_conversation(user_id, user_message, bot_response)
        return bot_response

chatbot = Chatbot()