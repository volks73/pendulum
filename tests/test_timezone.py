# -*- coding: utf-8 -*-

from pendulum import Pendulum

from . import AbstractTestCase


class TimezoneTest(AbstractTestCase):

    def test_set_timezone(self):
        d = Pendulum(2015, 1, 15, 18, 15, 34)
        now = Pendulum(2015, 1, 15, 18, 15, 34)
        self.assertEqual('UTC', d.timezone_name)
        self.assertPendulum(d, now.year, now.month, now.day, now.hour, now.minute)

        d.set_timezone('Europe/Paris')
        self.assertEqual('Europe/Paris', d.timezone_name)
        self.assertPendulum(d, now.year, now.month, now.day, now.hour + 1, now.minute)

    def test_to(self):
        d = Pendulum(2015, 1, 15, 18, 15, 34)
        now = Pendulum(2015, 1, 15, 18, 15, 34)
        self.assertEqual('UTC', d.timezone_name)
        self.assertPendulum(d, now.year, now.month, now.day, now.hour, now.minute)

        d.to('Europe/Paris')
        self.assertEqual('Europe/Paris', d.timezone_name)
        self.assertPendulum(d, now.year, now.month, now.day, now.hour + 1, now.minute)
