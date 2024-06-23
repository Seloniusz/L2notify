import asyncio
import io
import logging
import pyautogui
import pytesseract
import telegram
import time

# Set up bot tokens
bot_token = "XXX" # enter your token
chat_id = "XXX" # enter your chat_id
bot = telegram.Bot(token=bot_token)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up Tesseract OCR engine
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Get the position and size of the window you want to screenshot
window_title = "Lineage II"
window = pyautogui.getWindowsWithTitle(window_title)[0]
window_left, window_top, window_width, window_height = (
    window.left,
    window.top,
    window.width,
    window.height,
)

# Define cooldown duration (in seconds)
cooldown_duration = 30  # 30 seconds

# Initialize last_notification_time
last_notification_time = 0

# Readyness
logger.info(f" Up and running!")

# Continuously check for the appearance of "To Village" window
async def main():
    global last_notification_time
    while True:
        # Take a screenshot of the entire screen
        screenshot = pyautogui.screenshot()


        # Crop the screenshot to just the contents of the window
        window_screenshot = screenshot.crop(
            (
                window_left,
                window_top,
                window_left + window_width,
                window_top + window_height,
            )
        )

        # Perform OCR on the screenshot to recognize any text
        text = pytesseract.image_to_string(window_screenshot)


        # Check if "To the nearest town" window appears in the recognized text
        if "To the nearest town" in text:
            logger.info(f"Character dead, sending message")
            await send_notification("💀🔴 Your character is dead 💀", window_screenshot)
            

        # Check if "You have been disconnected from the server." appears in the recognized text
        elif "You have been disconnected from the server." in text:
            logger.info(f"Character disconnected, sending message")
            await send_notification(
                "🚫🛜 You have been disconnected from the server", window_screenshot
            )

        # Add a short delay before the next iteration
        await asyncio.sleep(1)


# Function to send notification
async def send_notification(message, screenshot):
    global last_notification_time
    # Check if cooldown period has elapsed
    if time.time() - last_notification_time >= cooldown_duration:
        # Send a message via Telegram
        try:
            await bot.send_message(chat_id=chat_id, text=message)
            logger.info(f"Notification sent: {message}")
            with io.BytesIO() as output:
                screenshot.save(output, format="PNG")
                output.seek(0)
                await bot.send_photo(chat_id=chat_id, photo=output)
            logger.info("Screenshot sent")
            # Update last_notification_time
            last_notification_time = time.time()
        except telegram.error.TelegramError as e:
            logger.error(f"Failed to send message: {e}")


asyncio.run(main())
