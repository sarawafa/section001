def main():
    # Part 1
    defense = 5
    attack = 8
    hp = 10

    if attack <= defense:
        print(f'No damage, since the defense stat is too high.')
    else:
        damage = attack - defense
        hp -= damage
        print(f'{damage} damage inflicted, enemy HP is now {hp}.')

    # Part 2
    lab_mark = 9
    midterm_mark = 40
    final_exam_mark = 135

    # Scale the marks
    scaled_lab_mark = (lab_mark / 10) * 30
    scaled_midterm_mark = (midterm_mark / 80) * 30
    scaled_exam_mark = (final_exam_mark / 180) * 40

    # Calculate final mark out of 100
    final_mark = scaled_lab_mark + scaled_midterm_mark + scaled_exam_mark

    # Determine letter grade
    if final_mark < 50:
        print("This student's final grade is F.")
    elif 50 <= final_mark < 60:
        print("This student's final grade is D.")
    elif 60 <= final_mark < 70:
        print("This student's final grade is C.")
    elif 70 <= final_mark < 80:
        print("This student's final grade is B.")
    else:
        print("This student's final grade is A.")
    # Part 3
    long_string = 'the quick brown fox'

    vowel_count = 0
    consonant_count = 0

    for char in long_string:
        if char in 'aeiou':
            vowel_count += 1
        elif char != ' ':
            consonant_count += 1

    ratio = round(vowel_count / consonant_count, 2)

    # Ensure the output matches the format exactly
    print(f"The vowel to consonant ratio of 'the quick brown fox' is {vowel_count} / {consonant_count} = {ratio:.2f}.")


if __name__ == "__main__":
    main()