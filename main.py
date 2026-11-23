import time
import random

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "To be or not to be, that is the question.",
    "All that glitters is not gold.",
]

def measure_accuracy(user_input, test_sentence):
    correct_chars = sum(1 for a, b in zip(user_input, test_sentence) if a == b)
    accuracy = (correct_chars / len(test_sentence)) * 100
    return accuracy


def typing_test():
    test_sentence = random.choice(sentences)
    print("Type the following sentence as fast as you can:")
    print(f"\n{test_sentence}\n")
    input("Press Enter when you're ready to start...")
    start_time = time.time()
    user_input = input("\nStart typing:\n ")
    end_time = time.time()
    time_taken = end_time - start_time

    words=len(test_sentence.split())

    print("Results:")
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Words typed: {words}")
    print(f"Typing speed: {words / (time_taken / 60):.2f} words per minute")
    accuracy = measure_accuracy(user_input, test_sentence)
    print(f"Accuracy: {accuracy:.2f}%")

typing_test()