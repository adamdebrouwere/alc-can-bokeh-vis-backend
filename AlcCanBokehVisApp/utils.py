from django.http import JsonResponse
from django.conf import settings
from functools import wraps
import os
import pandas as pd
from asgiref.sync import sync_to_async

def load_csv(file_path):
    full_path = os.path.join(settings.BASE_DIR, file_path)
    try:
        return pd.read_csv(full_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {full_path}")
    except Exception as e:
        raise Exception(f"Error reading {full_path}: {e}")


def handle_error(view_func):
    if not callable(view_func):
        raise ValueError("The decorated object must be callable.")

    @wraps(view_func)
    async def async_wrapper(request, *args, **kwargs):
        try:
            return await view_func(request, *args, **kwargs)
        except FileNotFoundError as e:
            return JsonResponse({"error": str(e)}, status=404)
        except Exception as e:
            return JsonResponse({"error": "An unexpected error occurred: " + str(e)}, status=500)

    return async_wrapper


async def generate_response(generator_func, *args, **kwargs):
    """
    Generate a response asynchronously using the provided generator function.
    """
    response = await sync_to_async(generator_func)(*args, **kwargs)
    return response
