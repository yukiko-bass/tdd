class TestCase:
    def __init__(self, name):
        self.name = name

    def set_up(self):
        pass

    def run(self):
        result = TestResult()
        result.test_started()
        self.set_up()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.test_failed()
        self.tear_down()
        return result

    def tear_down(self):
        pass


class TestResult:
    def __init__(self):
        self.run_count = 0
        self.error_count = 0

    def test_started(self):
        self.run_count = self.run_count + 1

    def test_failed(self):
        self.error_count = self.error_count + 1

    def summary(self):
        return "%d run, %d failed" % (self.run_count, self.error_count)


class WasRun(TestCase):
    def set_up(self):
        self.log = "set_up "

    def test_method(self):
        self.log = self.log + "test_method "

    def test_broken_method(self):
        raise Exception

    def tear_down(self):
        self.log = self.log + "tear_down "


class TestCaseTest(TestCase):
    def test_template_method(self):
        test = WasRun("test_method")
        test.run()
        assert("set_up test_method tear_down " == test.log)

    def test_result(self):
        test = WasRun("test_method")
        result = test.run()
        assert("1 run, 0 failed" == result.summary())

    def test_failed_result(self):
        test = WasRun("test_broken_method")
        result = test.run()
        assert("1 run, 1 failed" == result.summary())

    def test_failed_result_formatting(self):
        result = TestResult()
        result.test_started()
        result.test_failed()
        assert("1 run, 1 failed" == result.summary())


print(TestCaseTest("test_template_method").run().summary())
print(TestCaseTest("test_result").run().summary())
print(TestCaseTest("test_failed_result").run().summary())
print(TestCaseTest("test_failed_result_formatting").run().summary())
