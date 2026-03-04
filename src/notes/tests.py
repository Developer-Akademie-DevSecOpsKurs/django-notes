from django.test import TestCase, Client
from django.urls import reverse

from .models import Note, NotesUser


class NotesUserModelTest(TestCase):
    fixtures = ["notes_fixture.json"]

    def test_notesuser_username(self):
        user = NotesUser.objects.get(pk=1)
        self.assertEqual(user.username, "admin")

    def test_notesuser_phone_number(self):
        user = NotesUser.objects.get(pk=1)
        self.assertEqual(user.phone_number, "1234567890")

    def test_notesuser_is_superuser(self):
        user = NotesUser.objects.get(pk=1)
        self.assertTrue(user.is_superuser)

    def test_notesuser_is_staff(self):
        user = NotesUser.objects.get(pk=1)
        self.assertTrue(user.is_staff)

    def test_notesuser_str(self):
        user = NotesUser.objects.get(pk=1)
        self.assertEqual(str(user), "admin")

    def test_notesuser_regular_user_not_staff(self):
        user = NotesUser.objects.get(pk=2)
        self.assertFalse(user.is_staff)

    def test_notesuser_has_timestamps(self):
        user = NotesUser.objects.get(pk=1)
        self.assertIsNotNone(user.created_at)
        self.assertIsNotNone(user.updated_at)


class NoteModelTest(TestCase):
    fixtures = ["notes_fixture.json"]

    def test_note_title(self):
        note = Note.objects.get(pk=1)
        self.assertEqual(note.title, "First Note")

    def test_note_description(self):
        note = Note.objects.get(pk=1)
        self.assertEqual(note.description, "This is the first test note.")

    def test_note_str(self):
        note = Note.objects.get(pk=1)
        self.assertEqual(str(note), "1")

    def test_note_created_by(self):
        note = Note.objects.get(pk=1)
        self.assertEqual(note.created_by.username, "admin")

    def test_note_has_timestamps(self):
        note = Note.objects.get(pk=1)
        self.assertIsNotNone(note.created_at)
        self.assertIsNotNone(note.updated_at)

    def test_note_cascade_delete(self):
        user = NotesUser.objects.get(pk=2)
        user.delete()
        self.assertFalse(Note.objects.filter(pk=2).exists())

    def test_notes_count(self):
        self.assertEqual(Note.objects.count(), 2)


class NoteAdminTest(TestCase):
    fixtures = ["notes_fixture.json"]

    def setUp(self):
        self.client = Client()
        self.admin_user = NotesUser.objects.get(pk=1)
        self.client.force_login(self.admin_user)

    def test_note_admin_list_view(self):
        url = reverse("admin:notes_note_changelist")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_note_admin_change_view(self):
        url = reverse("admin:notes_note_change", args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_notesuser_admin_list_view(self):
        url = reverse("admin:notes_notesuser_changelist")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_notesuser_admin_change_view(self):
        url = reverse("admin:notes_notesuser_change", args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
