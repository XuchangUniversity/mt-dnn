from data_utils.metrics import calc_metrics

def eval_model(model, data, collater, metric_meta, use_cuda=True, with_label=True, label_mapper=None):
    if use_cuda:
        model.cuda()
    predictions = []
    golds = []
    scores = []
    ids = []
    metrics = {}
    for batch_info, batch_data in data:
        batch_info, batch_data = collater.patch_data(batch_info, batch_data)
        score, pred, gold = model.predict(batch_info, batch_data)
        predictions.extend(pred)
        golds.extend(gold)
        scores.extend(score)
        ids.extend(batch_info['uids'])
    if with_label:
        metrics = calc_metrics(metric_meta, golds, predictions, scores, label_mapper)
    return metrics, predictions, scores, golds, ids
