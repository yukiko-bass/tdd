class TestCase:
    def __init__(self, name):
        self.name = name

    def set_up(self):
        pass

    def run(self):
        self.set_up()
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def set_up(self):
        self.was_run = None
        self.was_set_up = 1

    def test_method(self):
        self.was_run = 1


class TestCaseTest(TestCase):
    def set_up(self):
        self.test = WasRun("test_method")

    def test_running(self):
        self.test.run()
        assert(self.test.was_run)

    def test_set_up(self):
        self.test.run()
        assert(self.test.was_set_up)


TestCaseTest("test_running").run()
TestCaseTest("test_set_up").run()
