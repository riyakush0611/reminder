import streamlit as st
import time

st.title('WhatsApp Image Sender with Reminder')

def send_image(MobileNo, image_path, Caption, interval_minutes):
    try:
        # Import pywhatkit only when needed
        import pywhatkit
        
        count = 0
        while True:
            pywhatkit.sendwhats_image(MobileNo, image_path, Caption, 20)
            st.write(f"Message sent to {MobileNo}")
            count += 1
            time.sleep(interval_minutes * 60)  # Convert minutes to seconds
            if count == 5:
                break
    except KeyboardInterrupt:
        st.write("\nMessage sending stopped.")
    except Exception as e:
        st.error(f"Error occurred: {str(e)}")

def main():
    MobileNo = st.text_input('Enter Mobile No:', '+919044705293')
    image_path = st.file_uploader('Upload Image:', type=['jpg', 'jpeg', 'png'])
    Caption = st.text_input('Enter Caption:', 'नीली गोली खाओ')
    interval_minutes = st.number_input('Enter Reminder Interval (minutes):', min_value=1, value=1)

    # Send Image button
    if st.button('Send Image'):
        if image_path is not None:
            send_image(MobileNo, image_path, Caption, interval_minutes)
        else:
            st.write("Please upload an image.")

    # Additional functionality for setting reminder time
    st.subheader('Set Reminder Time (Optional)')
    reminder_time = st.time_input('Select Time:')
    if reminder_time:
        st.write(f"Reminder set for {reminder_time.hour}:{reminder_time.minute}")

        # Convert reminder time to minutes
        current_time = time.localtime()
        reminder_minutes = (reminder_time.hour - current_time.tm_hour) * 60 + (reminder_time.minute - current_time.tm_min)
        
        if reminder_minutes < 0:
            reminder_minutes += 24 * 60
        
        st.write(f"Reminder in {reminder_minutes} minutes")

        if st.button('Set Reminder'):
            time.sleep(reminder_minutes * 60)  # Sleep until reminder time
            st.write(f"Reminder: Send image to {MobileNo}!")

if __name__ == "__main__":
    main()
