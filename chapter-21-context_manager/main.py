import context

with context.ClassWithContext("Joe") as cc:
    cc.print_name()