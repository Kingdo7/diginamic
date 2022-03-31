from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def comparator_profile(user, friend):
    # user c'est nous request.user ,,,,, friend # profile de la personne sur laquelle on clic
    ma_liste_amis = user.userprofile.friendlist.all()
    #             user--|--profile--|--list des amis du profile
    for each in ma_liste_amis:
        if friend == each.friend:
            if each.is_accepted:
                return mark_safe(
                    f'<a href="/account/remove-friend/{each.pk}" class="btn btn-danger"> Supprimer amis</a>')
            else:
                return mark_safe(f'<button class="btn btn-info"> en attente </button>')

    return mark_safe(
        f'<a href="/account/add-friend/{friend.user.userprofile.pk}" class="btn btn-success"> Ajouter amis</a>')
