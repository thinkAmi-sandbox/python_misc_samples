class Parent:
    def reply(self):
        print '[parent - reply]{}'.format(type(self))
        self.say()

    def say(self):
        print '[parent - say  ]{}'.format(type(self))
        print 'parent!'


class Child1(Parent):
    def reply(self):
        print '[child  - reply]{}'.format(type(self))
        Parent.reply(self)

    def say(self):
        print '[child  - say  ]{}'.format(type(self))
        print 'child1!'


class Child2(Parent):
    def reply(self):
        print '[child  - reply]{}'.format(type(self))
        super(Child2, self).reply()

    def say(self):
        print '[child  - say  ]{}'.format(type(self))
        print 'child2!'


if __name__ == '__main__':
    print '--- parent reply --->'
    p = Parent()
    p.reply()
    print '--- child1 reply --->'
    c1 = Child1()
    c1.reply()
    print '--- child2 reply --->'
    c2 = Child2()
    c2.reply()

    # =>
    # --- parent reply --->
    # [parent - reply]<type 'instance'>
    # [parent - say  ]<type 'instance'>
    # parent!
    # --- child1 reply --->
    # [child  - reply]<type 'instance'>
    # [parent - reply]<type 'instance'>
    # [child  - say  ]<type 'instance'>
    # child1!
    # --- child2 reply --->
    # [child  - reply]<type 'instance'>
    # Traceback (most recent call last):
    #   File "py2_old_style.py", line 40, in <module>
    #     c2.reply()
    #   File "py2_old_style.py", line 24, in reply
    #     super(Child2, self).reply()
    # TypeError: super() argument 1 must be type, not classobj
