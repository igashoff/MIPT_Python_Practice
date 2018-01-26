import sys
import argparse


class MyError(Exception):
    pass


class ParamsError(MyError):
    pass


class ContentError(MyError):
    pass


def putword(output, current_word, line_len, w):
    if line_len + len(current_word) <= w:
        output.write(current_word)
        line_len = line_len + len(current_word)
        if line_len + 1 <= w:
            output.write(' ')
            line_len += 1
    elif len(current_word) <= w:
        line_len = 0
        output.write('\n' + current_word)
        line_len = line_len + len(current_word)
        if line_len + 1 <= w:
            output.write(' ')
            line_len += 1
    else:
        raise ContentError('Max length of word is bigger than line length.')
    return line_len


def format_text(input, output, w, b):
    if b > w:
        raise ParamsError('Indention length is bigger than line length.')
    indent = ' ' * b
    punctuatiom_marks = [',', '.', '?', '!', '-', ':', '’']
    current_word = ''
    text = input.read()
    pos = 0
    new_word_flag = False
    paragraph_flag = 0
    line_len = b
    output.write(indent)
    while pos < len(text):
        char = text[pos]
        if char is '\n':
            paragraph_flag += 1
        elif char is ' ':
            new_word_flag = True
        elif char in punctuatiom_marks:
            new_word_flag = True
            current_word += char

        else:
            if paragraph_flag != 0:
                if paragraph_flag == 1:
                    line_len = putword(output, current_word, line_len, w)
                    current_word = ''
                    new_word_flag = False
                else:
                    line_len = putword(output, current_word, line_len, w)
                    current_word = ''
                    output.write('\n' + indent)
                    line_len = b
                paragraph_flag = 0
                new_word_flag = False
            else:
                if new_word_flag is True:
                    line_len = putword(output, current_word, line_len, w)
                    current_word = ''
                    new_word_flag = False
            current_word += char
        pos += 1
    line_len = putword(output, current_word, line_len, w)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i', '--input',
        default=None,
        help='Name for input file.'
    )
    parser.add_argument(
        '-o', '--output',
        default=None,
        help='Name for output file.'
    )
    parser.add_argument(
        '-l', '--line-length',
        default='90',
        help='Line length for formatted text.'
    )
    parser.add_argument(
        '-p', '--paragraph-spaces',
        default='5',
        help='Indention length for new paragraph. '
    )
    args = parser.parse_args()
    fin = sys.stdin if args.input is None else open(args.input, 'r')
    fout = sys.stdout if args.output is None else open(args.output, 'w')
    w = int(args.line_length)
    b = int(args.paragraph_spaces)
    try:
        format_text(fin, fout, w, b)
    except ParamsError as error:
        print('ParamsError:', error)
        raise SystemExit(1)
    except ContentError as error:
        print('ContentError:', error)
        raise SystemExit(1)
    fin.close()
    fout.close()

if __name__ == '__main__':
    main()
