from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase, Client
from django.urls import reverse

from .models import Note, NotesUser


class NotesUserModelTest(TestCase):
    fixtures = ["notes_fixture.json"]

    # --- admin user (pk=1) ---

    def test_success_admin_user_username(self):
        user = NotesUser.objects.get(pk=1)
        self.assertEqual(user.username, "admin")

    def test_success_admin_user_phone_number(self):
        user = NotesUser.objects.get(pk=1)
        self.assertEqual(user.phone_number, "1234567890")

    def test_success_admin_user_is_superuser(self):
        user = NotesUser.objects.get(pk=1)
        self.assertTrue(user.is_superuser)

    def test_success_admin_user_is_staff(self):
        user = NotesUser.objects.get(pk=1)
        self.assertTrue(user.is_staff)

    def test_success_admin_user_is_active(self):
        user = NotesUser.objects.get(pk=1)
        self.assertTrue(user.is_active)

    def test_success_admin_user_str_representation(self):
        user = NotesUser.objects.get(pk=1)
        self.assertEqual(str(user), "admin")

    def test_success_admin_user_has_timestamps(self):
        user = NotesUser.objects.get(pk=1)
        self.assertIsNotNone(user.created_at)
        self.assertIsNotNone(user.updated_at)

    # --- regular user (pk=2) ---

    def test_success_regular_user_username(self):
        user = NotesUser.objects.get(pk=2)
        self.assertEqual(user.username, "testuser")

    def test_success_regular_user_phone_number(self):
        user = NotesUser.objects.get(pk=2)
        self.assertEqual(user.phone_number, "9876543210")

    def test_success_regular_user_is_not_superuser(self):
        user = NotesUser.objects.get(pk=2)
        self.assertFalse(user.is_superuser)

    def test_success_regular_user_is_not_staff(self):
        user = NotesUser.objects.get(pk=2)
        self.assertFalse(user.is_staff)

    def test_success_regular_user_is_active(self):
        user = NotesUser.objects.get(pk=2)
        self.assertTrue(user.is_active)

    def test_success_regular_user_str_representation(self):
        user = NotesUser.objects.get(pk=2)
        self.assertEqual(str(user), "testuser")

    def test_success_regular_user_has_timestamps(self):
        user = NotesUser.objects.get(pk=2)
        self.assertIsNotNone(user.created_at)
        self.assertIsNotNone(user.updated_at)

    # --- aggregate / edge cases ---

    def test_success_total_user_count(self):
        self.assertEqual(NotesUser.objects.count(), 2)

    def test_failure_get_nonexistent_user_raises_exception(self):
        with self.assertRaises(ObjectDoesNotExist):
            NotesUser.objects.get(pk=999)


class NoteModelTest(TestCase):
    fixtures = ["notes_fixture.json"]

    # --- first note (pk=1, owned by admin) ---

    def test_success_first_note_title(self):
        note = Note.objects.get(pk=1)
        self.assertEqual(note.title, "First Note")

    def test_success_first_note_description(self):
        note = Note.objects.get(pk=1)
        self.assertEqual(note.description, "This is the first test note.")

    def test_success_first_note_str_representation(self):
        note = Note.objects.get(pk=1)
        self.assertEqual(str(note), "1")

    def test_success_first_note_created_by_admin_user(self):
        note = Note.objects.get(pk=1)
        self.assertEqual(note.created_by.username, "admin")

    def test_success_first_note_has_timestamps(self):
        note = Note.objects.get(pk=1)
        self.assertIsNotNone(note.created_at)
        self.assertIsNotNone(note.updated_at)

    # --- second note (pk=2, owned by regular user) ---

    def test_success_second_note_title(self):
        note = Note.objects.get(pk=2)
        self.assertEqual(note.title, "Second Note")

    def test_success_second_note_description(self):
        note = Note.objects.get(pk=2)
        self.assertEqual(note.description, "This is the second test note.")

    def test_success_second_note_str_representation(self):
        note = Note.objects.get(pk=2)
        self.assertEqual(str(note), "2")

    def test_success_second_note_created_by_regular_user(self):
        note = Note.objects.get(pk=2)
        self.assertEqual(note.created_by.username, "testuser")

    def test_success_second_note_has_timestamps(self):
        note = Note.objects.get(pk=2)
        self.assertIsNotNone(note.created_at)
        self.assertIsNotNone(note.updated_at)

    # --- aggregate / edge cases ---

    def test_success_total_note_count(self):
        self.assertEqual(Note.objects.count(), 2)

    def test_success_notes_filtered_by_admin_user(self):
        admin = NotesUser.objects.get(pk=1)
        self.assertEqual(Note.objects.filter(created_by=admin).count(), 1)

    def test_success_notes_filtered_by_regular_user(self):
        regular = NotesUser.objects.get(pk=2)
        self.assertEqual(Note.objects.filter(created_by=regular).count(), 1)

    def test_success_cascade_delete_removes_note_of_deleted_user(self):
        NotesUser.objects.get(pk=2).delete()
        self.assertFalse(Note.objects.filter(pk=2).exists())

    def test_success_cascade_delete_keeps_note_of_other_user(self):
        NotesUser.objects.get(pk=2).delete()
        self.assertTrue(Note.objects.filter(pk=1).exists())

    def test_failure_get_nonexistent_note_raises_exception(self):
        with self.assertRaises(ObjectDoesNotExist):
            Note.objects.get(pk=999)


class NoteAdminTest(TestCase):
    fixtures = ["notes_fixture.json"]

    def setUp(self):
        self.client = Client()
        self.admin_user = NotesUser.objects.get(pk=1)
        self.regular_user = NotesUser.objects.get(pk=2)
        self.client.force_login(self.admin_user)

    # --- Note admin list view ---

    def test_success_admin_note_list_view_returns_200(self):
        url = reverse("admin:notes_note_changelist")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # --- Note admin change views (one per fixture record) ---

    def test_success_admin_first_note_change_view_returns_200(self):
        url = reverse("admin:notes_note_change", args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_success_admin_second_note_change_view_returns_200(self):
        url = reverse("admin:notes_note_change", args=[2])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # --- NotesUser admin list view ---

    def test_success_admin_notesuser_list_view_returns_200(self):
        url = reverse("admin:notes_notesuser_changelist")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # --- NotesUser admin change views (one per fixture record) ---

    def test_success_admin_admin_user_change_view_returns_200(self):
        url = reverse("admin:notes_notesuser_change", args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_success_admin_regular_user_change_view_returns_200(self):
        url = reverse("admin:notes_notesuser_change", args=[2])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # --- edge cases ---

    def test_failure_non_staff_user_cannot_access_note_admin_list(self):
        self.client.force_login(self.regular_user)
        url = reverse("admin:notes_note_changelist")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_failure_non_staff_user_cannot_access_notesuser_admin_list(self):
        self.client.force_login(self.regular_user)
        url = reverse("admin:notes_notesuser_changelist")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_failure_admin_change_view_for_nonexistent_note_returns_302(self):
        url = reverse("admin:notes_note_change", args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_failure_admin_change_view_for_nonexistent_user_returns_302(self):
        url = reverse("admin:notes_notesuser_change", args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
