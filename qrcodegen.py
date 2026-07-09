import qrcode

#Taking UPI ID As A INPUT
upi_id = input("Enter your UPI ID: ")

#upi://pay?pa=UPI_Id&PN=Amount&cu=CURRENCY&TN=MESSAGE
#Defineing the payment URL based on the UPI ID and the payment app
#You can modify these URLs based on the payment app you want to support

phonepe_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
paytm_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"
google_pay_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"

#Creating QR Codes for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#Save the QRcode to image file (optional)
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
google_pay_qr.save("google_pay_qr.png")

#Display the QR code s (you may to install PTL/Pillow Library)
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()
