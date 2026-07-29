# SPDX-License-Identifier: GPL-3.0-only

import unittest

from distributed_work_events import (
    NODE_ADVERTISEMENT_PUBLISHED,
    WORK_ACCEPTED,
    WORK_COMPLETED,
    WORK_OFFERED,
)
from ghost.distributed_body_run import run_distributed_ghost


class DistributedBodyGhostRunTests(unittest.TestCase):
    def test_real_cross_repo_contracts_complete_the_ghost_run(self):
        result = run_distributed_ghost()

        self.assertEqual(result.cognitive_outcome, "intent_candidate")
        self.assertEqual(result.placed_node_id, "ruby-lyra-01")
        self.assertEqual(result.placed_organ, "ruby")
        self.assertEqual(result.placement_mode, "primary")
        self.assertTrue(result.runtime_completed)
        self.assertIn("Observation only; no response was executed", result.queen_result.summary)

    def test_lifecycle_is_advertise_offer_accept_complete(self):
        result = run_distributed_ghost()

        self.assertEqual(
            result.lifecycle_events,
            (
                NODE_ADVERTISEMENT_PUBLISHED,
                NODE_ADVERTISEMENT_PUBLISHED,
                WORK_OFFERED,
                WORK_ACCEPTED,
                WORK_COMPLETED,
            ),
        )
        self.assertEqual(result.receipt_events, result.lifecycle_events)
        self.assertEqual(len(result.queen_result.receipt_ids), 5)
        self.assertEqual(len(set(result.queen_result.receipt_ids)), 5)

    def test_important_result_returns_to_queen_without_authority(self):
        result = run_distributed_ghost()

        self.assertTrue(result.queen_result.important)
        self.assertEqual(result.queen_result.source_organ, "ruby")
        self.assertEqual(result.queen_result.authority, "none")
        self.assertFalse(result.canonical)
        self.assertFalse(result.execution_authorized)
        self.assertFalse(result.actuation_authorized)
        self.assertEqual(result.authority, "none")

    def test_same_inputs_preserve_the_same_structural_result(self):
        first = run_distributed_ghost()
        second = run_distributed_ghost()

        self.assertEqual(first.cognitive_outcome, second.cognitive_outcome)
        self.assertEqual(first.intent_statement, second.intent_statement)
        self.assertEqual(first.placed_node_id, second.placed_node_id)
        self.assertEqual(first.placement_mode, second.placement_mode)
        self.assertEqual(first.lifecycle_events, second.lifecycle_events)
        self.assertEqual(first.queen_result.summary, second.queen_result.summary)


if __name__ == "__main__":
    unittest.main()
