from django.shortcuts import render, redirect
from .models import Student
from .models import  Student, Candidate, Vote   
def home(request):
    return render(request, 'home.html')

def student_login(request):
    if request.method == 'POST':
        roll_no = request.POST['roll_no']

        try:
            student = Student.objects.get(roll_no=roll_no)

            request.session['student_id'] = student.id

            return redirect('candidate_list')

        except Student.DoesNotExist:
            return render(request, 'student_login.html', {
                'error': 'Invalid Roll Number'
            })

    return render(request, 'student_login.html')

def candidate_list(request):
    candidates = Candidate.objects.all()

    return render(request,
                  'candidate_list.html',
                  {'candidates': candidates})

def vote_candidate(request, candidate_id):

    student_id = request.session.get('student_id')

    if not student_id:
        return redirect('student_login')

    student = Student.objects.get(id=student_id)

    if student.has_voted:
        return render(request,
                      'message.html',
                      {'message': 'You have already voted!'})

    candidate = Candidate.objects.get(id=candidate_id)

    Vote.objects.create(
        student=student,
        candidate=candidate
    )

    candidate.votes += 1
    candidate.save()

    student.has_voted = True
    student.save()

    return render(request,
                  'message.html',
                  {'message': 'Vote submitted successfully!'})