# coding: utf-8
from __future__ import print_function
from __future__ import unicode_literals

from transaction import *
from collections import namedtuple

TestExpectation = namedtuple("TransactionTestResult", 
    ["debtor", "creditor", "value", "currency", "notes"])

def run_test(testcase):
    result = Transaction(testcase[0])
    expectation = testcase[1]

    assert result.debtor == expectation.debtor, "incorrect debtor"
    assert result.creditor == expectation.creditor, "incorrect creditor"
    assert result.value == expectation.value, "incorrect value"
    assert result.currency == expectation.currency, "incorrect currency"
    assert result.notes == expectation.notes, "incorrect notes"


test_cases = [
    ('<@U024H4SR1> -&gt; <@U024H5LFB> $15 (thai food)',
    TestExpectation('U024H4SR1', 'U024H5LFB', '15', None, ' (thai food)')
        ),
    ('<@U024H5KK7> -&gt; <@U024H5LFB> 20$',
        TestExpectation('U024H5KK7', 'U024H5LFB', '20', None, None))
    ]


def main():
    for test in test_cases:
        try:
            run_test(test)
        except AssertionError as err:
            print(err, test, Transaction(test[0]))

    print("%d tests passed" % len(test_cases))

if __name__ == "__main__":
    main()