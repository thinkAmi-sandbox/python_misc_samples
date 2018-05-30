class Parent:
    def reply(self):
        print('[parent - reply]{}'.format(type(self)))
        self.say()

    def say(self):
        print('[parent - say  ]{}'.format(type(self)))
        print('parent!')


class Child1(Parent):
    def reply(self):
        print('[child  - reply]{}'.format(type(self)))
        super().reply()

    def say(self):
        print('[child  - say  ]{}'.format(type(self)))
        print('child1!')


class Child2(Parent):
    def reply(self):
        print('[child  - reply]{}'.format(type(self)))
        super(Child2, self).reply()

    def say(self):
        print('[child  - say  ]{}'.format(type(self)))
        print('child2!')


class Child3(Parent):
    def reply(self):
        print('[child  - reply]{}'.format(type(self)))
        Parent.reply(self)

    def say(self):
        print('[child  - say  ]{}'.format(type(self)))
        print('child3!')


if __name__ == '__main__':
    print('--- parent reply --->')
    p = Parent()
    p.reply()
    print('--- child1 reply --->')
    c1 = Child1()
    c1.reply()
    print('--- child2 reply --->')
    c2 = Child2()
    c2.reply()
    print('--- child3 reply --->')
    c3 = Child3()
    c3.reply()
    
    # =>
    # --- parent reply --->
    # [parent - reply]<class '__main__.Parent'>
    # [parent - say  ]<class '__main__.Parent'>
    # parent!
    # --- child1 reply --->
    # [child  - reply]<class '__main__.Child1'>
    # [parent - reply]<class '__main__.Child1'>
    # [child  - say  ]<class '__main__.Child1'>
    # child1!
    # --- child2 reply --->
    # [child  - reply]<class '__main__.Child2'>
    # [parent - reply]<class '__main__.Child2'>
    # [child  - say  ]<class '__main__.Child2'>
    # child2!
    # --- child3 reply --->
    # [child  - reply]<class '__main__.Child3'>
    # [parent - reply]<class '__main__.Child3'>
    # [child  - say  ]<class '__main__.Child3'>
    # child3!
