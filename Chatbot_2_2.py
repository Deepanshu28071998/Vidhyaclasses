from nltk.chat.util import Chat, reflections

# Updated response pairs specific to the coaching institute chatbot
pairs = [
    # Greeting and Introduction
    [
        r"(hi, i am (.*)|hi i am (.*)|my name is (.*)|hlo i am (.*)|hi,i m (.*)|hi i m (.*)|hlo i m (.*)|hlo, my name is (.*)|hi, my name is (.*))",
        ["Hello %1! Welcome to our Coaching Institute. How can I assist you today?"]
    ],
    [
        r"hi|hello|Whats up|hi dear",
        ["Hello! How can I help you today?"]
    ],
    [
        r"nameste|namaskar|good morning",
        ["Namaste! How may I assist you?"]
    ],
    
    # Asking about courses
    [
        r"(.*)(course|courses|programs|classes)(.*)",
        ["We offer various courses like Mathematics, Science, English, and Computer Science. Would you like more details about a specific course?"]
    ],
    [
        r"(.*)(Batch|batch|batches|Batches)(.*)",
        ["We have different batches for different courses. Which course are you interested in? We have Academic batches and also Competitive batches."]
    ],

    # Asking about fees
    [
        r"(.*)(fee|fees|tuition|cost)(.*)",
        ["The fee structure varies depending on the course. Can you specify the course you are interested in?"]
    ],
    
    # Asking about schedule
    [
        r"(.*)(schedule|timing|class hours|timings)(.*)",
        ["Our classes are scheduled both in the morning and evening. For specific course timings, please mention the course name."]
    ],
    
    # Thank you
    [
        r"thank you|thanku|thanx|thx|thank you very much|thankyou|thanks",
        ["You're welcome! Happy to help."]
    ],
    
    # Inquiry about services
    [
        r"(i have a)(query|problem|question|issue)(.*)",
        ["Please feel free to ask your question! I'm here to help."]
    ],
    
    # Asking about chatbot's well-being
    [
        r"how are you",
        ["I am just a chatbot, but I'm functioning well! How can I assist you today?"]
    ],

    # User is feeling well
    [
        r"i am good|i'm good|i am fine|i'm fine|i feel good|i am doing well",
        ["That's great to hear! How can I assist you today?"]
    ],
    
    # Asking for contact details or support
    [
        r"(.*)(contact|support|help)(.*)",
        ["You can reach out to us at our support email: vidhyaclassesbijnor183@gmail.com or call us at +91 8057509745, +91 9058113227."]
    ],

    # User ends the conversation
    [
        r"bye|goodbye|see you|exit",
        ["Goodbye! Feel free to reach out anytime. Have a great day!"]
    ],

    [
        r"canyou gave me details of coaching|coaching details|details about your coaching|give me the details of vidhya classes",
        ["Our coaching classes are conducted by experienced teachers. We provide coaching for classes 6th to 12th and also provide Competitive batches like UP police, Railways, UPTET, NEET, SSC and more."]
    ]
]

def bot():
    print("Hi, I am the Vidhya classes Coaching Institute Chatbot. How can I assist you today?")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    bot()
