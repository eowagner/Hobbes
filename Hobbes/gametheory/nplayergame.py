from django.shortcuts import get_object_or_404
from publicgoods.models import Game_Instance, Game_Response
from decimal import Decimal

def get_game_outcome_context(instance_id):
    instance = get_object_or_404(Game_Instance, pk=instance_id)
    players = Game_Response.objects.filter(game_id=instance)
    
    strats = list(map(lambda x: x.contribution, players))

    outcome = public_goods_game_payouts(instance.pot_multiplier, instance.endowment, strats)

    results = [ {'player': players[i], 'payout': outcome[5][i]} for i in range(len(players)) ]

    context = {
            'instance': instance,
            'number_responses': outcome[0],
            'total_contribution': outcome[1],
            'total_pot': outcome[2],
            'return_per_player': outcome[3],
            'results': results
            }

    return context;

def public_goods_game_payouts(pot_multiplier, endowment, strats):
    num_players = len(strats)
    total_contribution = sum(strats)
    total_pot = round(Decimal(pot_multiplier) * Decimal(total_contribution),2)
    
    return_per_player = 0

    if num_players > 0:
        return_per_player = round(total_pot/num_players,2)

    payouts = [endowment - strats[i] + return_per_player for i in range(num_players)]

    return (num_players, total_contribution, total_pot, return_per_player, strats, payouts)
