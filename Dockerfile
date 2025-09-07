FROM public.ecr.aws/lambda/python:3.8

WORKDIR /var/task

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Change ownership
RUN chown -R 1000:1000 /var/task

# Handler in src/subdirectory
CMD ["src.handler.handle"]  # For src/handler.py with handle function
