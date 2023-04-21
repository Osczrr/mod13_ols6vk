import unittest
import app
import datetime

class TestSymbol(unittest.TestCase):

#symbol: capitalized, 1-7 alpha characters
    def test_symbol(self):
        # Valid Uppercase Symbol
        app.SetStockSymbol("GOOGL")
        self.assertEqual(app.GetStockSymbol(), "GOOGL")
        # Valid lowercase Symbol
        app.SetStockSymbol("googl")
        self.assertEqual(app.GetStockSymbol(), "googl")

    def test_invalid_symbol(self):
        # Invalid Symbol With Over 7 characters
        with self.assertRaises(ValueError):
            app.SetStockSymbol("SymbolOver7Characters")
        # Invalid Symbol with Non-alpha character (not numbers)
        with self.assertRaises(ValueError):
            app.SetStockSymbol("GOO#@")
        # Invalid Symbol with Numbers
        with self.assertRaises(ValueError):
            app.SetStockSymbol("GO123")
        


#chart type: 1 numeric character, 1 or 2 
    def test_chart(self):
        # Valid Chart type "1"
        app.SetChartType("1")
        self.assertEqual(app.GetChartType(), "1")
        # Valid Chart type "2"
        app.SetChartType("2")
        self.assertEqual(app.GetChartType(), "2")

    def test_invalid_chart(self):
        # Invalid Chart type 5
        app.SetChartType("5")
        self.assertEqual(app.GetChartType(),"5")
        # Invalid Chart type "#"
        with self.assertRaises(ValueError):
            app.SetChartType("#")


#time series: 1 numeric character, 1 - 4
    def test_time(self):
        # Valid Time Series "1"
        app.SetTimeSeries("1")
        self.assertEqual(app.GetTimeSeries(),"1")
        # Valid Time Series "2"
        app.SetTimeSeries("2")
        self.assertEqual(app.GetTimeSeries(),"2")
        # Valid Time Series "3"
        app.SetTimeSeries("3")
        self.assertEqual(app.GetTimeSeries(),"3")
        # Valid Time Series "4"
        app.SetTimeSeries("4")
        self.assertEqual(app.GetTimeSeries(),"4")

    def test_invalid_time(self):
        # Invalid Time Series "#"
        with self.assertRaises(ValueError):
            app.SetTimeSeries("#")
        # Invalid Time Series "5"
        with self.assertRaises(ValueError):
            app.SetTimeSeries("5")
        # Invalid Time Series Multiple characters
        with self.assertRaises(ValueError):
            app.SetTimeSeries("23")
        

#start date: date type YYYY-MM-DD
    def test_beg_date(self):
        # Valid Date Format
        app.SetStockSymbol("GOOGL")
        date_str = "2017-12-10"
        try:
            datetime.datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            self.fail("Incorrect date format")
        app.SetDates(date_str)
        self.assertEqual(app.SetDates(), date_str)
        self.assertEqual(app.GetBeginningDate(), date_str)

    def test_invalid_beg_date(self):
        # Invalid Valid Date Format
        app.SetStockSymbol("GOOGL")
        date_str = "10-12-2017"
        try:
            datetime.datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            self.fail("Incorrect date format")
        app.SetDates(date_str)
        self.assertEqual(app.SetDates(), date_str)
        self.assertEqual(app.GetBeginningDate(), date_str)


#end date: date type YYYY-MM-DD
    def test_end_date(self):
        # Valid Date Format
        app.SetStockSymbol("GOOGL")
        date_str = "2017-12-10"
        try:
            datetime.datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            self.fail("Incorrect date format")
        app.SetDates(date_str)
        self.assertEqual(app.SetDates(), date_str)
        self.assertEqual(app.GetEndDate(), date_str)

    def test_invalid_beg_date(self):
        # Invalid Valid Date Format
        app.SetStockSymbol("GOOGL")
        date_str = "10-12-2017"
        try:
            datetime.datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            self.fail("Incorrect date format")
        app.SetDates(date_str)
        self.assertEqual(app.SetDates(), date_str)
        self.assertEqual(app.GetEndDate(), date_str)


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestSymbol)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
