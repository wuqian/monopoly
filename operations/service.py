from operations.models import *

def update_mechine_stat(op_id, mechine_id, from_stat_id, to_stat_id):
    op = Operator.objects.get(pk=op_id)
    mechine = Mechine.objects.get(pk=mechine_id)
    from_stat = MechineStat.objects.get(pk=from_stat_id)
    to_stat = MechineStat.objects.get(pk=to_stat_id)

    #TODO: check mechine stat is none busy
    #create MechineUsageRecord
    # stat : 0 -> idle, 1 -> busy
    MechineUsageRecord.objects.create(op=op, mechine=mechine,
                                    from_stat=from_stat, to_stat=to_stat)
