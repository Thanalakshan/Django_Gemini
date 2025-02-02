import json, os
import google.generativeai as gen_ai
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from dotenv import load_dotenv
from django.utils.safestring import mark_safe
load_dotenv()

# Initialize the Gemini API model with the API key from settings.py
def initialize_chat_session():
    try:
        gen_ai.configure(api_key=os.getenv('GEMINI_API_KEY'))

        # Specify the model you want to use (e.g., 'gemini-pro' or any other available model)
        model = gen_ai.GenerativeModel('gemini-pro')  # Adjust the model name as necessary

        # Create and return a chat session
        chat_session = model.start_chat(history=[])
        return chat_session
        
    except Exception as e:
        print(f"Error initializing chat session: {e}")
        return None

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in!")
            return redirect('index')
        else:
            messages.error(request, "Invalid credentials. Please try again.")
            return redirect('login')

    return render(request, 'chatbot/login.html')

# Signup View
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')
        else:
            messages.error(request, form.errors.as_text())
            return redirect('signup')

    else:
        form = UserCreationForm()

    return render(request, 'chatbot/signup.html', {'form': form})

# Home Page (Index)
@login_required
def index(request):
    return render(request, 'chatbot/index.html')

# Logout View
def user_logout(request):
    logout(request)
    return redirect('login')

# Chat View (CSRF exempt, login required)
@csrf_exempt
@login_required
def chat(request):
    # Create the chat session instance
    chat_session = initialize_chat_session()

    if chat_session is None:
        return JsonResponse({'response': 'Error initializing chat session.'}, status=500)

    if request.method == 'POST':
        # Get the user input from the request
        data = json.loads(request.body)
        user_input = data.get('input_text')

    if user_input:
        try:
            # Send the user input to Gemini API and get the response
            gemini_response = chat_session.send_message(user_input)
            response_text = gemini_response.text
            formatted_response = mark_safe(response_text)  # This ensures the response is rendered as HTML

            return JsonResponse({'response': formatted_response})
        except Exception as e:
            print(f"Error during chat message processing: {e}")
            return JsonResponse({'response': f'Error processing message: {e}'}, status=500)

    return JsonResponse({'response': 'Please provide input text.'}, status=400)
