#Program: Check OTP matches or not

print("===== OTP VERIFICATION =====")

correctOtp = "5678"
attempt = ""

# Keep asking until matching OTP
while attempt != correctOtp:
    attempt = input("Enter OTP: ")

print("OTP verified successfully.")
