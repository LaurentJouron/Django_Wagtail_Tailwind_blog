from django.shortcuts import render, redirect


def home_index_view(request):
    return redirect("blog/")
