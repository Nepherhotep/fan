import asyncio
import argparse


parser = argparse.ArgumentParser(description='fan commandline client')
parser.add_argument('cmd', nargs='*', help='command to execute')


async def run_cmd(cmd):
    ctx = 'get_ctx'
    full_cmd = 'ctx.rpc.{}'.format(cmd)
    print('eval: {}'.format(full_cmd))


def main():
    args = parser.parse_args()
    print('ARGS: {}'.format(args))

    loop = asyncio.get_event_loop()
    task = asyncio.ensure_task(run_cmd(args.cmd[0]))
    loop.run_until_complete(task)
