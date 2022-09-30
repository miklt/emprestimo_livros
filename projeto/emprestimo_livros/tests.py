from django.test import TestCase

# Create your tests here.
from emprestimo_livros.models import Livro, Usuario, Emprestimo

class LivroModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Livro.objects.create(titulo='Os Irmãos Karamazov',isbn='000000')
    def test_criacao_id(self):
        livro_1 = Livro.objects.get(titulo='Os Irmãos Karamazov')
        self.assertEqual(livro_1.id, 1)
class UsuarioModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Usuario.objects.create(nome="Michelet")

    def test_criacao_id(self):
        usuario_1 = Usuario.objects.get(nome="Michelet")
        self.assertEqual(usuario_1.id, 1)

class EmprestimoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Usuario.objects.create(nome="Michelet")
        Livro.objects.create(titulo='Os Irmãos Karamazov')
        livro_1 = Livro.objects.get(titulo='Os Irmãos Karamazov')
        usuario_1 = Usuario.objects.get(nome="Michelet")
        Emprestimo.objects.create(livro=livro_1, usuario=usuario_1)
    def test_criacao_emprestimo_id(self):
        emprestimo_1 = Emprestimo.objects.get(id=1)
        self.assertEqual(emprestimo_1.usuario.id,1)
