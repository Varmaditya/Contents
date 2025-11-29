#Program: Check OTP matches or not

print("===== OTP VERIFICATION =====")

correct_otp = "5678"
attempt = ""

# Keep asking until matching OTP
while attempt != correct_otp:
    attempt = input("Enter OTP: ")

print("OTP verified successfully.")
