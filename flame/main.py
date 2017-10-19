from transformations import LinearTransformation

def main():
    t1 = LinearTransformation.generate();
    print(t1.matrix)


if __name__ == '__main__':
    main()