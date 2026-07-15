def main():
    def take_args_kwargs(*args, **kwargs):
        print(f"""args are: {args}\nkwargs are: {kwargs}""")
    take_args_kwargs("list",
                     "set",
                     "world",
                     a=1,
                     b=2)

if __name__ == "__main__":
    main()
