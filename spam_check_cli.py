from joblib import load

def main():
    # Load the saved pipeline
    pipeline = load("spam_pipeline.pkl")
    
    print("📬 Spam Message Detector (type 'exit' to quit)\n")

    while True:
        msg = input("📝 Enter a message: ")
        if msg.lower() == "exit":
            print("👋 Exiting. Goodbye!")
            break

        prediction = pipeline.predict([msg])[0]
        result = "Spam" if prediction == 1 else "Ham"

        print(f"🔍 Prediction: {result}\n")

if __name__ == "__main__":
    main()

