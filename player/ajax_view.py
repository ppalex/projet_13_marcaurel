
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from core.models.player import Player, PlayerSubscription
import pdb

@login_required
def player_follow(request):

    if request.method == "POST":

        player_id = request.POST.get('player_id')
        action = request.POST.get('action')
        
        if player_id and action:
            player = Player.objects.get_player_by_id(player_id).first()
            try:
                pdb.set_trace()
                if action == 'follow':
                    PlayerSubscription.objects.get_or_create(
                        follower=request.user.player,
                        following=player)
                else:
                    PlayerSubscription.objects.get_player_following(
                        request.user.player, player)

                return JsonResponse({'status': 'ok'})
            except Player.DoesNotExist:
                return JsonResponse({'status': 'nok'})
    return JsonResponse({'status': 'nok'})
