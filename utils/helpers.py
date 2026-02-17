def print_results(score, keywords):
    print("\n========== MATCH RESULT ==========")
    print(f"Match Score: {score}%")
    print("\nTop Matching Keywords:")
    for kw in keywords:
        print(f"- {kw}")
    print("==================================\n")
