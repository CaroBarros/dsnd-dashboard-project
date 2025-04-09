# Import any dependencies needed to execute sql queries
from sqlite3 import connect
import pandas as pd
from sql_execution import QueryMixin

# Define a class called QueryBase
# Use inheritance to add methods
# for querying the employee_events database.
class QueryBase(QueryMixin):

    # Create a class attribute called `name`
    # set the attribute to an empty string
    name=""

    # Define a `names` method that receives
    # no passed arguments
    def names(self):
        
        # Return an empty list
        return []


    # Define an `event_counts` method
    # that receives an `id` argument
    # This method should return a pandas dataframe
    def event_counts(self, id):

        # QUERY 1
        # Write an SQL query that groups by `event_date`
        # and sums the number of positive and negative events
        # Use f-string formatting to set the FROM {table}
        # to the `name` class attribute
        # Use f-string formatting to set the name
        # of id columns used for joining
        # order by the event_date column
        sql_query = f"""
        SELECT
            e.event_date,
            SUM(positive_events) AS positive events,
            SUM(negative_events) AS negative events
        FROM {self.name} AS e
        WHERE e.{self.name}_id = {id}  
        GROUP BY e.event_date
        ORDER BY e.event_date
        """
        return self.pandas_query(sql_query)
            
    

    # Define a `notes` method that receives an id argument
    # This function should return a pandas dataframe
    def notes (self, id):

        # QUERY 2
        # Write an SQL query that returns `note_date`, and `note`
        # from the `notes` table
        # Set the joined table names and id columns
        # with f-string formatting
        # so the query returns the notes
        # for the table name in the `name` class attribute
        sql_query = f"""
        SELECT 
            n.note_date,
            n.note
        FROM notes as n
        JOIN {self.name} as e
        ON e.{self.name}_id = n.{self.name}_id
        WHERE e.{self.name}_id ={id}
        ORDER BY n.note_date;
        """

        return self.pandas_query(sql_query)

