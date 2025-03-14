"""
   scoremipsum demo test
"""
import sys

import ops


# import scoremipsum

# from scoremipsum import scoremipsum


def main():
    """
    scoremipsum demo
    """
    print("="*80)
    print('(scoremipsum demo) :: demo ::')
    print("-"*80)

    #   display the supported sports list
    #
    ops.sportsball()

    # scoremipsum.help()

    # commands = scoremipsum.commands()
    # print(f"== {commands=}")
    print("-"*80)

    # sports = scoremipsum.sports()
    # print(f"== {sports=}")
    print("-"*80)

    print('(scoremipsum demo) :: end ::')
    print("="*80)
    return 0


# ----------------------------------------
if __name__ == '__main__':
    main()
    sys.exit(0)
