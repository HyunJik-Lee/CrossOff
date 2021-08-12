from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from mandalart.models import *
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.utils.translation import gettext_lazy as _
from django.core import serializers
from django.utils import timezone

User = get_user_model()


@login_required
def calendar(request, id):
    user = User.objects.get(id=id)
    blocks = Block.objects.filter(user=user, created_date__year=timezone.now().year)
    blockList = []
    specount = 0
    blocksObj = serializers.serialize('json', blocks, fields=('content', 'created_date', 'spelist'))

    BigGoalList = []
    if not user.is_manda:
        return redirect('mandalart:new')
    manda = Mandalart.objects.get(user=user.id)
    big = BigGoal.objects.get(manda=manda)
    BigGoalList.append((big.content, big.is_achieved))
    mid = MidGoal.objects.filter(big=big).order_by('id')
    MidGoalList = []
    SpecificGoalDict = {}
    for i in range(len(mid)):
        SpecificGoalList = []
        MidGoalList.append(mid[i].content)
        spe = SpecificGoal.objects.filter(mid=mid[i]).order_by('id')
        for j in range(len(spe)):
            SpecificGoalList.append(spe[j].content)
        SpecificGoalDict[i] = SpecificGoalList
    return render(
        request, 'daily/calendar.html', {
            'manda_mid': json.dumps(MidGoalList, ensure_ascii=False),
            'manda_small': json.dumps(SpecificGoalDict, ensure_ascii=False),
            'blocks': blocksObj,
        })


def addBlock(request):
    u = request.user
    block = Block(user=u, content=request.POST['content'])
    block.save()
    spelist = Spelist(block=block)
    spelist.save()
    spes = request.POST.getlist('spes')
    for spe in spes:
        item = Item(spelist=spelist, specificgoal=u.mandalart.biggoal.midgoal.all()[int(spe[0])].specificgoal.all()[int(spe[1])])
        item.save()
    return redirect('/daily/calendar/' + str(request.user.id))
