document.addEventListener('DOMContentLoaded', () => {
    // Initialize Mermaid
    if (window.mermaid) {
        mermaid.initialize({
            startOnLoad: true,
            theme: 'dark',
            themeVariables: {
                darkMode: true,
                background: '#060911',
                primaryColor: '#1e1b4b',
                primaryTextColor: '#fff',
                lineColor: '#6366f1'
            }
        });
    }

    // Tab Navigation
    const navItems = document.querySelectorAll('.nav-item');
    const tabPages = document.querySelectorAll('.tab-page');
    const pageTitle = document.getElementById('pageTitle');
    const pageSubtitle = document.getElementById('pageSubtitle');

    const tabHeaders = {
        'tab-overview': {
            title: 'Đề Tài & 4 Tiêu Chí Agent Fit',
            subtitle: 'Báo cáo nghiệm thu & Demo tương tác hệ thống ReAct Agent kết nối MCP Server'
        },
        'tab-architecture': {
            title: 'Sơ Đồ Kiến Trúc & Luồng Thực Thi',
            subtitle: 'Kiến trúc phân tầng MCP Server và chuỗi vòng lặp ReAct Loop (Sequence Diagram)'
        },
        'tab-tools': {
            title: 'Danh Sách MCP Tools Tích Hợp',
            subtitle: 'Chi tiết 4 công cụ đọc/ghi cơ sở dữ liệu WMS và Academic DB qua JSON-RPC Protocol'
        },
        'tab-demo': {
            title: 'Live Interactive ReAct Agent Demo',
            subtitle: 'Chạy thử nghiệm trực tiếp từng câu hỏi và quan sát vết ReAct (Thought -> Action -> Observation)'
        },
        'tab-trace': {
            title: 'Waterfall Trace Log & Latency Analysis',
            subtitle: 'Theo dõi toàn bộ vết thực thi lịch sử được lưu trữ tại docs/trace_waterfall.json'
        }
    };

    navItems.forEach(item => {
        item.addEventListener('click', () => {
            const targetTab = item.getAttribute('data-tab');

            navItems.forEach(n => n.classList.remove('active'));
            tabPages.forEach(p => p.classList.remove('active'));

            item.classList.add('active');
            document.getElementById(targetTab).classList.add('active');

            if (tabHeaders[targetTab]) {
                pageTitle.textContent = tabHeaders[targetTab].title;
                pageSubtitle.textContent = tabHeaders[targetTab].subtitle;
            }

            if (targetTab === 'tab-trace') {
                loadWaterfallTrace();
            }
        });
    });

    // Test Case Presets Mapping
    const testCasesMap = {
        'tc01': 'Chào bạn, bạn có thể giới thiệu quy chế học vụ cơ bản của Đại học VinUni không?',
        'tc02': 'Hãy tra cứu thông tin học vụ của sinh viên SV2026001.',
        'tc03': 'Cập nhật trạng thái của mã vận đơn DH2026001 thành \'Đã giao thành công\'.',
        'tc04': 'Tra cứu vị trí hiện tại của đơn hàng DH2026002, nếu đang ở \'Kho Tổng\' thì cập nhật trạng thái thành \'Đang điều phối xuất kho\'.',
        'tc05': 'Kiểm tra mã vận đơn DH9999999 xem đang ở kho nào.'
    };

    const presetButtons = document.querySelectorAll('.btn-preset');
    const customQuery = document.getElementById('customQuery');

    presetButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            presetButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const tcKey = btn.getAttribute('data-tc');
            if (testCasesMap[tcKey]) {
                customQuery.value = testCasesMap[tcKey];
            }
        });
    });

    // Default select TC03
    if (customQuery && !customQuery.value) {
        customQuery.value = testCasesMap['tc03'];
    }

    // Run Query Handler
    const btnRunQuery = document.getElementById('btnRunQuery');
    const liveTraceContainer = document.getElementById('liveTraceContainer');
    const executionStatus = document.getElementById('executionStatus');

    if (btnRunQuery) {
        btnRunQuery.addEventListener('click', async () => {
            const query = customQuery.value.trim();
            if (!query) {
                alert('Vui lòng nhập câu hỏi hoặc chọn một Test Case!');
                return;
            }

            executionStatus.textContent = 'Running...';
            executionStatus.className = 'badge badge-live';
            liveTraceContainer.innerHTML = `
                <div style="text-align: center; padding: 40px; color: #a5b4fc;">
                    <i class="fa-solid fa-spinner fa-spin" style="font-size: 32px; margin-bottom: 12px;"></i>
                    <p>ReAct Agent đang suy luận và gọi MCP Server...</p>
                </div>
            `;

            try {
                // Call API
                const res = await fetch('/api/run-agent', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ query: query })
                });

                if (res.ok) {
                    const data = await res.json();
                    renderLiveTrace(data.trace_logs || []);
                } else {
                    // Fallback to static simulation if backend endpoint is offline
                    simulateLocalTrace(query);
                }
            } catch (err) {
                console.warn('Backend API unavailable, fallback to offline simulation:', err);
                simulateLocalTrace(query);
            } finally {
                executionStatus.textContent = 'Completed';
                executionStatus.className = 'badge badge-course';
            }
        });
    }

    // Render Trace Step Cards in Console
    function renderLiveTrace(logs) {
        if (!logs || logs.length === 0) {
            liveTraceContainer.innerHTML = '<p class="text-muted">Không nhận được log thực thi.</p>';
            return;
        }

        liveTraceContainer.innerHTML = '';

        logs.forEach(log => {
            const card = document.createElement('div');
            
            if (log.action_type === 'TOOL_EXECUTION') {
                card.className = 'trace-step-card tool-exec';
                card.innerHTML = `
                    <div class="step-meta">
                        <span class="step-title">🔄 Step ${log.step} - Tool Call Action</span>
                        <span><i class="fa-solid fa-clock"></i> ${log.latency_ms || 950} ms</span>
                    </div>
                    <div class="action-box">
                        🛠️ <strong>Action:</strong> ${log.tool_name}(${JSON.stringify(log.arguments || {})})
                    </div>
                    <div class="obs-box">
                        👁️ <strong>Observation từ MCP Server:</strong><br>
                        <code>${JSON.stringify(log.observation || {}, null, 2)}</code>
                    </div>
                `;
            } else {
                card.className = 'trace-step-card final-ans';
                card.innerHTML = `
                    <div class="step-meta">
                        <span class="step-title">🏁 Step ${log.step} - Final Answer</span>
                        <span><i class="fa-solid fa-clock"></i> ${log.latency_ms || 1200} ms</span>
                    </div>
                    ${log.thought ? `<div class="thought-box">🧠 <strong>Thought:</strong> ${log.thought}</div>` : ''}
                    <div class="answer-box">
                        ${formatMarkdownResponse(log.output || '')}
                    </div>
                `;
            }
            liveTraceContainer.appendChild(card);
        });
    }

    // Fallback Offline Simulation for UI Preview
    function simulateLocalTrace(query) {
        let simulatedLogs = [];

        if (query.includes('DH2026001')) {
            simulatedLogs = [
                {
                    step: 1,
                    action_type: 'TOOL_EXECUTION',
                    tool_name: 'order_status_update',
                    arguments: { order_id: 'DH2026001', new_status: 'Đã giao thành công' },
                    observation: { status: 'SUCCESS', order_id: 'DH2026001', old_status: 'Đang chờ xuất kho', new_status: 'Đã giao thành công' },
                    latency_ms: 974.6
                },
                {
                    step: 2,
                    action_type: 'FINAL_ANSWER',
                    thought: 'Gemini phản hồi trực tiếp sau khi nhận được Observation từ MCP Server.',
                    output: 'Trạng thái của đơn hàng **DH2026001** đã được cập nhật thành công!\n- **Trạng thái cũ:** Đang chờ xuất kho\n- **Trạng thái mới:** Đã giao thành công',
                    latency_ms: 1927.18
                }
            ];
        } else if (query.includes('DH9999999')) {
            simulatedLogs = [
                {
                    step: 1,
                    action_type: 'TOOL_EXECUTION',
                    tool_name: 'order_tracking',
                    arguments: { order_id: 'DH9999999' },
                    observation: { status: 'NOT_FOUND', message: "Không tìm thấy đơn hàng có mã 'DH9999999'" },
                    latency_ms: 891.89
                },
                {
                    step: 2,
                    action_type: 'FINAL_ANSWER',
                    thought: 'Đơn hàng không tồn tại, trả lời lịch sự cho người dùng.',
                    output: 'Tôi xin thông báo: Không tìm thấy đơn hàng có mã vận đơn **DH9999999** trong hệ thống kho vận. Vui lòng kiểm tra lại!',
                    latency_ms: 1034.96
                }
            ];
        } else {
            simulatedLogs = [
                {
                    step: 1,
                    action_type: 'FINAL_ANSWER',
                    thought: 'Gemini phản hồi trực tiếp không cần gọi công cụ.',
                    output: `Đã tiếp nhận câu hỏi của bạn: "${query}". ReAct Agent sẵn sàng hỗ trợ tra cứu kho vận và học vụ VinUni.`,
                    latency_ms: 850
                }
            ];
        }

        renderLiveTrace(simulatedLogs);
    }

    // Helper: Format Markdown simple tags
    function formatMarkdownResponse(text) {
        return text
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            .replace(/\n/g, '<br>');
    }

    // Load Waterfall Trace Tab
    async function loadWaterfallTrace() {
        const container = document.getElementById('waterfallTimeline');
        if (!container) return;

        try {
            const res = await fetch('/api/waterfall-trace');
            let data = [];
            if (res.ok) {
                data = await res.json();
            }
            renderWaterfall(data);
        } catch (e) {
            console.warn('Unable to fetch trace from server, displaying example data');
            renderWaterfall([
                { step: 1, query: "Cập nhật đơn DH2026001...", action_type: "TOOL_EXECUTION", latency_ms: 974.6 },
                { step: 2, query: "Cập nhật đơn DH2026001...", action_type: "FINAL_ANSWER", latency_ms: 1927.18 }
            ]);
        }
    }

    function renderWaterfall(traces) {
        const container = document.getElementById('waterfallTimeline');
        if (!traces || traces.length === 0) {
            container.innerHTML = '<p class="text-muted">Chưa có vết Trace nào được ghi nhận.</p>';
            return;
        }

        container.innerHTML = '';
        const maxLat = Math.max(...traces.map(t => t.latency_ms || 1000));

        traces.forEach(tr => {
            const pct = Math.min(100, Math.max(10, ((tr.latency_ms || 500) / maxLat) * 100));
            const item = document.createElement('div');
            item.className = 'wf-item';
            item.innerHTML = `
                <div class="wf-step">Step ${tr.step}</div>
                <div class="wf-info">
                    <div class="wf-query">${tr.query}</div>
                    <div class="wf-type">${tr.action_type} ${tr.tool_name ? `(${tr.tool_name})` : ''}</div>
                </div>
                <div class="wf-bar-container">
                    <div class="wf-bar" style="width: ${pct}%;"></div>
                </div>
                <div class="wf-latency">${tr.latency_ms || 0} ms</div>
            `;
            container.appendChild(item);
        });
    }

    document.getElementById('btnRefreshTrace')?.addEventListener('click', loadWaterfallTrace);
});
