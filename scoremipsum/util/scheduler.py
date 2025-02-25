#
#   SCOREM
#
"""
scheduler
----------

scheduler utils for the `scoremipsum` module.
"""


def grouper(inputs, n=2):
    """

    :param inputs:
    :param n:
    :return:
    """
    iters = [iter(inputs)] * n
    return zip(*iters)
