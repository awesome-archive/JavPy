# encoding: utf-8

from JavPy.sources.javmodel_com import JavModelCom
from JavPy.sources.warashi_asian_pornstars_fr import WarashiAsianPornStarsFr
from JavPy.utils.requester import spawn_many, Task
from future.builtins import filter
from JavPy.utils.common import cache


class ActressTranslate:
    sources_en2jp = [JavModelCom, WarashiAsianPornStarsFr]

    @staticmethod
    @cache
    def translate2jp(actress):
        res = list(filter(lambda x: x, spawn_many(
            [Task(source.translate2jp, actress) for source in ActressTranslate.sources_en2jp]
        ).wait_for_one_finished()))
        if not res:
            return None
        else:
            return res[0]


if __name__ == '__main__':
    print(ActressTranslate.translate2jp('Eimi Fukada'))
