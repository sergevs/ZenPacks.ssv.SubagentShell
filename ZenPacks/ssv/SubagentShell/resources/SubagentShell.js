(function(){

var ZC = Ext.ns('Zenoss.component');

function render_link(ob) {
    if (ob && ob.uid) {
        return Zenoss.render.link(ob.uid);
    } else {
        return ob;
    }
}

ZC.CommandStatusPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'CommandStatus',
            autoExpandColumn: 'name',
            fields: [
                {name: 'uid'},
                {name: 'severity'},
                {name: 'status'},
                {name: 'name'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitored'},
                {name: 'monitor'},
                {name: 'locking'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name')
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                width: 65,
                sortable: true
            },{
                id: 'status',
                dataIndex: 'status',
                header: _t('Status'),
                width: 60
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                width: 65
            }]
        });

        ZC.CommandStatusPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('CommandStatusPanel', ZC.CommandStatusPanel);
ZC.registerName('CommandStatus', _t('CommandStatus'), _t('CommandStatus'));

})();
