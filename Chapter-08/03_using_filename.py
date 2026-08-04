import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="server.log",
    format="%(asctime)s - %(message)s - %(levelname)s",
)


logger = logging.getLogger()

logger.setLevel(logging.DEBUG)


# নতুন লাইন করে একটা গ্যাপ নিয়ে আউটপুট দিবে । (server.log  ফাইলে)
logging.info("\n")

logger.debug("Harmless Debug Message")
logger.info("This is an Info Message")
logger.warning("warning......!!!")
logger.error("Devide by Zero")
logger.critical("Server is down!!")





"""
Working Process
---------------

1. import logging
   → logging Module Import করা হয়েছে।

2. logging.basicConfig(...)
   → Logger Configure করা হয়েছে।
   - filename="server.log" → Output 'server.log' File-এ Save হবে।
   - level=logging.DEBUG → DEBUG এবং এর উপরের সব Log Save হবে।
   - format=... → Date, Time, Message এবং Log Level-এর Format নির্ধারণ করে।

3. logger = logging.getLogger()
   → একটি Logger Object তৈরি করা হয়েছে।

4. logger.setLevel(logging.DEBUG)
   → Logger-এর Threshold DEBUG করা হয়েছে।

5. logging.info("\n")
   → Log File-এ একটি Blank Line যোগ করে, যাতে প্রতিটি Run-এর Output-এর মাঝে Gap থাকে।

6. logger.debug(), info(), warning(), error(), critical()
   → বিভিন্ন Log Level-এর Message 'server.log' File-এ লিখে।

How to Run
----------
1. File Save করো।
2. Terminal-এ Run করো:
   python 03_using_filename.py
   অথবা
   py 03_using_filename.py

Where is the Output?
--------------------
→ Terminal-এ Log দেখাবে না।
→ একই Folder-এর 'server.log' File খুলে Output দেখতে হবে।

How does the Output Update?
---------------------------
→ Program আবার Run করলেই 'server.log' Update হবে।

- filemode="a" (Default)
  → পুরোনো Log রেখে নতুন Log শেষে যোগ হবে।

- filemode="w"
  → প্রতিবার Run করলে পুরোনো Log মুছে নতুন Log লেখা হবে।
"""
