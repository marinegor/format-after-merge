import click


def summator(nums):
    return sum(map(int, nums))

@click.command()
@click.argument('nums', nargs=-1)
@click.option('--action', default='sum', help='Which action to perform (mul or sum)')
@click.option('--numpy', default=False, help='Perform this using numpy', is_flag=True)
def crunch(nums, action, numpy):
    """Simple program that performs action on numbers"""
    if numpy:
        import numpy as np
        nums = np.array(list(map(int, nums)))
        if action == 'sum': rv = nums.sum()
        elif action == 'mul': rv = nums.prod()
        else: raise ValueError('wrong action')
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
