import os
import click

plugin_folder = os.path.join(os.path.dirname(__file__), 'commands')
print(plugin_folder)


class AcmeCommand(click.MultiCommand):

    def list_commands(self, ctx):
        commands = list()
        for filename in os.listdir(plugin_folder):
            if filename.endswith('.py'):
                rv.append(filename[:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        ns = {}
        fn = os.path.join(plugin_folder, name + '.py')
        with open(fn) as f:
            code = compile(f.read(), fn, 'exec')
            eval(code, ns, ns)
        return ns['cli']