import just_count.square
import click

@click.command()
@click.argument("square", type=int)
def sqrt(square):
    print(f"The square of {square} is {just_count.square.square(square)}")

if __name__ == '__main__':
    sqrt()
