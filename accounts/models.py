import re

from django.contrib.auth.models import AbstractUser, UserManager
from django.core import validators
from django.db import models
from localflavor.br.models import (
    BRCNPJField,
    BRCPFField,
    BRPostalCodeField,
    BRStateField,
)


class User(AbstractUser):
    """User model customizado. Usa email em vez de username para autenticar"""

    username = models.CharField(
        "Usuário",
        max_length=30,
        unique=True,
        validators=[
            validators.RegexValidator(
                re.compile("^[\w.@+-]+$"),
                "Informe um nome de usuário válido. "
                "Este valor deve conter apenas letras, números "
                "e os caracteres: @/./+/_ .",
                "invalid",
            )
        ],
        help_text="Um nome curto que será usado para identificá-lo de forma única.",
    )
    email = models.EmailField("Email", max_length=150, unique=True)
    cpf = BRCPFField("CPF", blank=True)
    cnpj = BRCNPJField("CNPJ", blank=True)
    postal_code = BRPostalCodeField("CEP", blank=True)
    address = models.CharField("Endereço", max_length=250, blank=True)
    district = models.CharField("Bairro", max_length=250, blank=True)
    state = BRStateField("Estado", blank=True)
    city = models.CharField("Cidade", max_length=250, blank=True)

    created = models.DateTimeField("Criado", auto_now_add=True)
    modified = models.DateTimeField("Modificado", auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = [
            "-created",
        ]

    def _str_(self):
        self.name or self.email
