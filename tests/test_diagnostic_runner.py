from datetime import datetime
from pathlib import Path

from pier.diagnose.models import DiagnosticItemResult
from pier.diagnose.runner import DiagnosticRunner
from pier.models.task.id import LocalTaskId
from pier.models.trial.result import AgentInfo, ExceptionInfo


def _diagnostic_item_result(
    *,
    diagnostic_result: dict | None,
    exception_info: ExceptionInfo | None = None,
) -> DiagnosticItemResult:
    return DiagnosticItemResult(
        source_trial_name="trial",
        diagnostic_trial_name="trial",
        task_name="task",
        task_id=LocalTaskId(path=Path("/tmp/task")),
        task_checksum="checksum",
        source_trial_uri="file:///tmp/source",
        diagnostic_trial_uri="file:///tmp/diagnostic",
        agent_info=AgentInfo(name="agent", version="1"),
        diagnostic_result=diagnostic_result,
        exception_info=exception_info,
    )


def test_reuse_clean_cached_diagnostic_result():
    result = _diagnostic_item_result(diagnostic_result={"ok": True})

    assert DiagnosticRunner._should_reuse_cached_result(result)


def test_retry_cached_diagnostic_result_with_exception():
    result = _diagnostic_item_result(
        diagnostic_result={"ok": True},
        exception_info=ExceptionInfo(
            exception_type="CancelledError",
            exception_message="",
            exception_traceback="traceback",
            occurred_at=datetime.now(),
        ),
    )

    assert not DiagnosticRunner._should_reuse_cached_result(result)


def test_retry_cached_metadata_without_diagnostic_result():
    result = _diagnostic_item_result(diagnostic_result=None)

    assert not DiagnosticRunner._should_reuse_cached_result(result)
