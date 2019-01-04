class TestCase:
    def __init__(self, name):
        self.name = name

    def set_up(self):
        pass

    def run(self):
        self.set_up()
        method = getattr(self, self.name)
        method()
        self.tear_down()

    def tear_down(self):
        pass


class WasRun(TestCase):
    def set_up(self):
        self.log = "set_up "

    def test_method(self):
        self.log = self.log + "test_method "

    def tear_down(self):
        self.log = self.log + "tear_down "

class TestCaseTest(TestCase):
    def test_template_method(self):
        self.test = WasRun("test_method")
        self.test.run()
        assert("set_up test_method tear_down " == self.test.log)


TestCaseTest("test_template_method").run()
