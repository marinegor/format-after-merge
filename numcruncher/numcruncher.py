import click


@click.command()
@click.argument('nums', nargs=-1)
@click.option('--action', default='sum', help='Which action to perform (mul or sum)')
def crunch(nums, action):
    """Simple program that performs action on numbers"""
    if action == 'sum':
        rv = sum(map(int, nums))
    elif action == 'mul':
        rv = 1
        for num in map(int, nums): rv *= num
    else:
        raise ValueError('wrong action')
    print(rv)

def main():
    crunch()
