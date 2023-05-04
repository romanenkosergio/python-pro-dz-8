from sqlite3 import ProgrammingError

from django.db import connections
from django.utils import timezone


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        # Create logs table if it does not exist
        with connections['logs'].cursor() as cursor:
            try:
                cursor.execute(
                    "CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY AUTOINCREMENT, path TEXT, method TEXT, "
                    "execution_time INTEGER, status_code INTEGER)")
            except ProgrammingError:
                # The table already exists
                pass

    def __call__(self, request):
        start_time = timezone.now()
        response = self.get_response(request)
        end_time = timezone.now()

        execution_time = (end_time - start_time).total_seconds() * 1000

        # Save log to file
        with open('log.txt', 'a') as f:
            f.write(
                f"Path: {request.path}, Method: {request.method}, Execution time: {execution_time}ms, "
                f"Status Code: {response.status_code}\n")

        # Save log to database
        with connections['logs'].cursor() as cursor:
            cursor.execute("INSERT INTO logs (path, method, execution_time, status_code) VALUES (%s, %s, %s, %s)",
                           [request.path, request.method, execution_time, response.status_code])

        return response
